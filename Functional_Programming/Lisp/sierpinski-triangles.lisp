(defun print-fractal (j)
  (loop for x
	from 1 to j do
	(let* ((ones (loop for y
			   from 1 to (1- (* 2 x))
			   collect 1)))
	  (format t "~v,,,'_@:<~{~d~}~>~%" 63 ones))))
