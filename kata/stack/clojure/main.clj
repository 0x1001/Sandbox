(ns stack)
(def stack (ref []))

(defn push [item]
    (dosync 
        (commute stack 
            (fn [stack] (conj stack item))
        )
    )
)

(defn pop []
    (dosync
        (def out (peek @stack))
        (commute stack clojure.core/pop)
        ((fn [] out))
    )
)

(defn size []
    (count @stack)
)

; Tests
(assert (= 0 (size)))
(push 1)
(assert (= 1 (size)))
(push 2)
(assert (= 2 (size)))
(assert (= 2 (pop)))
(assert (= 1 (size)))
(assert (= 1 (pop)))
(assert (= 0 (size)))
