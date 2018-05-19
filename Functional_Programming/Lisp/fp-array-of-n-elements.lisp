;; https://www.hackerrank.com/challenges/fp-array-of-n-elements/problem
(defun f (n)
  (labels ((foo (i acc)
		(cond ((= i 0) acc)
		      (t (foo (1- i) (append acc '(1)))))))
    (foo n ())))

(f (read))
