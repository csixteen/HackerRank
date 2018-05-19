;; https://www.hackerrank.com/challenges/fp-reverse-a-list/problem
(defun my-reverse ()
  (labels ((rev-rec (acc)
		    (let ((n (read *standard-input* nil)))
		      (cond ((null n) acc)
			    (t (rev-rec (cons n acc)))))))
    (rev-rec nil)))

(format t "~{~d~%~}" (my-reverse))
