;; https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list/problem
(defun solution ()
  (labels ((f (pos)
	      (let ((n (read *standard-input* nil)))
		(cond ((null n) nil)
		      ((evenp pos) (format t "~d~%" n) (f (1+ pos)))
		      (t (f(1+ pos)))))))
    (f 1)))

(solution)
