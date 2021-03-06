;; https://www.hackerrank.com/challenges/eval-ex/problem
;; Force the usage of double precision, as opposed to the default
;; single precision.
(setq *read-default-float-format* 'double-float)

(defun eval-ex (x)
  (labels ((fact (n) (if (= n 1) 1 (* n (fact (1- n))))))
    (+ 1 (loop for i
	       from 1 to 9
	       sum (/ (expt x i) (fact i))))))

(defun solution (n)
  (unless (<= n 0)
    (format t "~,4f~%" (eval-ex (read)))
    (solution (1- n))))

(solution (read))
