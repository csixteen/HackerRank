;; https://www.hackerrank.com/challenges/fp-update-list/problem
(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (cond ((null n) nil)
	  (t (cons n (read-list))))))

(format t "~{~d~%~}" (mapcar #'abs (read-list)))
