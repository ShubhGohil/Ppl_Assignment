(defparameter sum 1)
(defun factorial (num)
	(loop for x from 2 to num
		do(setq sum (* sum x))
	)
	(write sum)
)
		
(factorial (read))
(terpri)
