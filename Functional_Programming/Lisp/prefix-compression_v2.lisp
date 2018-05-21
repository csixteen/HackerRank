;; https://www.hackerrank.com/challenges/prefix-compression/problem
(defun prefix-compression (x y)
  (pref-comp x y ()))

(defun pref-comp (x y prefix)
  (cond ((or (or (= 0 (length x)) (= 0 (length y))) 
	     (not (equal (char x 0) (char y 0)))) 
	 (prefix-print x y prefix))
	(t (pref-comp (subseq x 1) (subseq y 1) (append prefix (list (char x 0)))))))

(defun prefix-print (x y prefix)
  (format t "~d ~{~C~}~%" (length prefix) prefix)
  (format t "~d ~A~%" (length x) x)
  (format t "~d ~A~%" (length y) y))

(prefix-compression (read-line) (read-line))
