;; https://www.hackerrank.com/challenges/fp-list-replication/problem
(defun f (n lst)
  (labels ((repeat (elem i)
		   (if (= i 0)
		     nil
		     (cons elem (repeat elem (1- i))))))
    (cond ((null lst) nil)
	  (t (append (repeat (car lst) n) (f n (cdr lst)))))))

(defun read-list ()
  (let ((n (read *standard-input* nil)))
    (if (null n)
      nil
      (cons n (read-list)))))

(format t "~{~d~%~}" (f (read) (read-list)))
