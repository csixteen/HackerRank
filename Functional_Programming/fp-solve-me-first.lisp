(defun solveMeFirst ()
  (let ((a (read-line))
	(b (read-line)))
    (write (+ (parse-integer a) (parse-integer b)))))

(solveMeFirst)
