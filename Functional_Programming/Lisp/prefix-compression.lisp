;; https://www.hackerrank.com/challenges/prefix-compression/problem
(defun prefix-compression (x y)
  (pref-comp (coerce x 'list) (coerce y 'list) ()))

(defun pref-comp (x y prefix)
  (cond ((or (and (null x) (null y))
	     (not (equal (car x) (car y))))
	 (prefix-print x y prefix))
	(t (pref-comp (cdr x) (cdr y) (append prefix (list (car x)))))))

(defun prefix-print (x y prefix)
  (format t "~d ~{~C~}~%" (length prefix) prefix)
  (format t "~d ~{~C~}~%" (length x) x)
  (format t "~d ~{~C~}~%" (length y) y))

(prefix-compression (read-line) (read-line))
