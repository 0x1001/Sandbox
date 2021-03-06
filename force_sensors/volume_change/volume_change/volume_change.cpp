// volume_change.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"

#define DllExport   __declspec(dllexport)

extern "C"
{
	DllExport int test_1(void)
	{
		return 1;
	}

	DllExport int change_volume(UINT8 * wave_1, UINT8 * wave_2, UINT32 wave_size, float volume_1, float volume_2, UINT8 *output, UINT32 *output_size)
	{
		INT32 s1_ch1; // First sound channel 1
		INT32 s1_ch2;
		INT32 s2_ch1; // Second sound channel 1
		INT32 s2_ch2;

		INT32 ch1;  // Combined channel 1 (sum of first wave ch1 and seconda wave ch1)
		INT32 ch2;  // Combined channel 2

		for (UINT32 i = 0; i < wave_size; i += 6) // Each sample is 3 bytes, there 2 channels. [sample_ch1_0, sample_ch2_0, sample_ch1_1, sample_ch2_1, sample_ch1_2, sample_ch2_2, ...]
		{
			s1_ch1 = 0;  
			s1_ch2 = 0;
			s2_ch1 = 0;  
			s2_ch2 = 0;
			
			ch1 = 0;
			ch2 = 0;

			s1_ch1 = (((INT32)wave_1[i + 0] << 8) | ((INT32)wave_1[i + 1] << 16) | ((INT32)wave_1[i + 2] << 24)) >> 8;  // 3 bytes per sample, signed integer. little endian. Mapped to three most significant bytes of integer because of sign, then shifted by one byte.
			s1_ch2 = (((INT32)wave_1[i + 3] << 8) | ((INT32)wave_1[i + 4] << 16) | ((INT32)wave_1[i + 5] << 24)) >> 8;

			s2_ch1 = (((INT32)wave_2[i + 0] << 8) | ((INT32)wave_2[i + 1] << 16) | ((INT32)wave_2[i + 2] << 24)) >> 8;
			s2_ch2 = (((INT32)wave_2[i + 3] << 8) | ((INT32)wave_2[i + 4] << 16) | ((INT32)wave_2[i + 5] << 24)) >> 8;

			ch1 = INT32(s1_ch1 * volume_1 + s2_ch1 * volume_2);
			ch2 = INT32(s1_ch2 * volume_1 + s2_ch2 * volume_2);

			// Ch1 - Conversion of integer to byte array. 3 bytes per sample. Most significant byte is ignored.
			output[i + 0] = ch1 & 0xFF;
			output[i + 1] = (ch1 >> 8) & 0xFF;
			output[i + 2] = (ch1 >> 16) & 0xFF;

			// Ch2
			output[i + 3] = ch2 & 0xFF;
			output[i + 4] = (ch2 >> 8) & 0xFF;
			output[i + 5] = (ch2 >> 16) & 0xFF;
		}

		output_size = &wave_size;

		return 0;
	}
}