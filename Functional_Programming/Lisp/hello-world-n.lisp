(defun helloWorldNTimes ()
  (let ((n (parse-integer (read-line))))
    (labels ((phw (x)
	     (cond ((= x 0) nil)
		   (t (format t "Hello World~%")
		      (phw (1- x))))))
      (phw n))))

(helloWorldNTimes)
