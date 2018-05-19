;; https://www.hackerrank.com/challenges/fp-sum-of-odd-elements/problem
(defun sum-odd (acc)
  (let ((n (read *standard-input* nil)))
    (cond ((null n) (format t "~d~%" acc))
	  ((oddp n) (sum-odd (+ n acc)))
	  (t (sum-odd acc)))))

(sum-odd 0)
