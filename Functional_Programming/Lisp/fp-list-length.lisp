;; https://www.hackerrank.com/challenges/fp-list-length/problem
(defun lst-length (acc)
  (let ((n (read *standard-input* nil)))
    (cond ((null n) (format t "~d~%" acc))
	  (t (lst-length (1+ acc))))))

(lst-length 0)
