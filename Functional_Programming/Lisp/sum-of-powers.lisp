(defun sum-of-powers (x n cur)
  (cond ((< x 0) 0)
	((= x 0) 1)
	((> cur x) 0)
	(t (+ (sum-of-powers (- x (expt cur n)) n (1+ cur))
	      (sum-of-powers x n (1+ cur))))))

(format t "~a~%" (sum-of-powers (read) (read) 1))
