(defun factorial (num)
	(if (= num 0) 1 
		(* num (factorial(- num 1)))
	)
)

(write (factorial (read)))
(terpri)
