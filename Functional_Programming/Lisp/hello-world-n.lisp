(defun helloWorldNTimes ()
  (let ((n (parse-integer (read-line))))
    (labels ((phw (x)
	     (when (> x 0)
		   (progn (format t "Hello World~%") 
			  (phw (1- x))))))
      (phw n))))

(helloWorldNTimes)
