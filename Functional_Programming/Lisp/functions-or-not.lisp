;; https://www.hackerrank.com/challenges/functions-or-not/problem
(defun functions-or-not ()
  (let ((x (read)))
    (labels ((f-or-not (n)
			(when (> n 0)
			  (if (f-or-n) 
			    (format t "YES~%") 
			    (format t "NO~%"))
			  (f-or-not (1- n)))))
      (f-or-not x))))

(defun split (s)
  (loop for i = 0 then (1+ j)
	as j = (position #\Space s :start i)
	collect (subseq s i j)
	while j))

(defun read-args (n)
  (if (= n 0)
    nil
    (let ((pair (split (read-line))))
      (cons (list (parse-integer (first pair)) (parse-integer (second pair))) 
	    (read-args (1- n))))))

(defun f-or-n ()
  (let* ((n (read))
	(args (read-args n))
	(domain (mapcar #'car args))
	(lenDomain (length domain)))
    (= lenDomain (length (remove-duplicates domain)))))

(functions-or-not)
