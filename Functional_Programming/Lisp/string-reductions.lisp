;; https://www.hackerrank.com/challenges/string-reductions/problem
(defun reduction (lst)
  (let ((previous (make-hash-table)))
    (labels ((f (l acc)
		(cond ((null l) acc)
		      ((null (gethash (car l) previous))
		       (setf (gethash (car l) previous) (car l))
		       (f (cdr l) (cons (car l) acc)))
		      (t (f (cdr l) acc)))))
      (coerce (reverse (f lst ())) 'string))))

(format t "~a~%" (reduction (coerce (read-line) 'list)))
