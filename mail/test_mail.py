import unittest


class Test_mail(unittest.TestCase):
    def test_mail(self):
        import mail
        import json
        from email import message

        with open("config.config") as fp:
            config = json.load(fp)

        message = message.Message()
        message["From"] = "test@test.rpi"
        message["To"] = "damian.nowok@gmail.com"
        message["Subject"] = "This is a test!"

        server = mail.TurboSmtp(config["user"], config["password"])
        server.send(message)


if __name__ == "__main__":
    unittest.main()
