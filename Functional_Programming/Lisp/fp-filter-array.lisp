;; https://www.hackerrank.com/challenges/fp-filter-array/problem
(defun solution (target)
  (labels ((f ()
	      (let ((n (read *standard-input* nil)))
		(cond ((null n) nil)
		      ((< n target) (format t "~d~%" n) (f))
		      (t (f))))))
    (f)))

(solution (read))
