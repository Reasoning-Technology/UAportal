;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.
(package-initialize)

;;--------------------------------------------------------------------------------
;; remote shell on RT server
;;
;;  (defun shell-rt ()
;;    (interactive)
;;    (let ((default-directory "/ssh:thomas_lynch@reasoningtechnology.com:"))
;;      (shell)))
;;
;;  (defun dired-rt ()
;;   (interactive)
;;   (dired "/user@192.168.1.5:/"))

;;--------------------------------------------------------------------------------
;; gdb
;;
;; fix 'feature' of broken gdb where it takes control of an emacs window, and locks the
;; user out from switching from it
;;
  (defun unlock-window ()
    "Turns off window dedication."
    (interactive)
    (set-window-dedicated-p (get-buffer-window (current-buffer)) nil)
    )


;;--------------------------------------------------------------------------------
;; json
;;
  (setq json-encoding-pretty-print t)
  (setq json-encoding-lisp-style-closings t)
  ;(setq json-encoding-lisp-style-closings nil)
  (defun wrap-comma ()
    "wrap end of line comma to first of next line"
    (interactive) 
    (while (re-search-forward "\\(.*\\), *\n\\( *\\)" nil t) (replace-match "\\1\n\\2,"))
    )

;;--------------------------------------------------------------------------------
;; rust
;;
;; (require 'package)
;; (add-to-list 'package-archives
;;            '("melpa-stable" . "https://stable.melpa.org/packages/"))
;; (package-initialize)
;; (package-refresh-contents)

;;(setq rust-indent-offset 2)
;;(require 'rust-mode)

;;--------------------------------------------------------------------------------
;; python
;;
  (add-hook 'python-mode-hook '(lambda () (setq python-indent 2)))

;;--------------------------------------------------------------------------------
;; Lisp
;;
  (setq lisp-indent-offset 2)
  (setq inferior-lisp-program "sbcl")      

  (modify-syntax-entry ?[ "(]" lisp-mode-syntax-table)
  (modify-syntax-entry ?] ")[" lisp-mode-syntax-table)
  (modify-syntax-entry ?{ "(}" lisp-mode-syntax-table)
  (modify-syntax-entry ?} "){" lisp-mode-syntax-table)

;;--------------------------------------------------------------------------------
;; Javascript
;;
  (setq js-indent-level 2)
  (setq css-indent-offset 2)    

;;--------------------------------------------------------------------------------
;; extended character set for programming examples in the TTCA book
;;
;; preferable to have keys for the characters, but the keyboard is already overloaded ..
;; (define-key key-translation-map (kbd "<f9> p") (kbd "¬"))
;; (set-input-method “latin-9-prefix)

  (global-set-key [f1] 'help-command)
  (global-set-key "\C-h" 'nil)
  (define-key key-translation-map (kbd "M-S") (kbd "§"))

  (global-set-key (kbd "C-x g phi SPC") [?φ]) ; phi for phase
  (global-set-key (kbd "C-x g Phi SPC") [?Φ]) 

  (global-set-key (kbd "C-x g d SPC") [?δ])
  (global-set-key (kbd "C-x g D SPC") [?Δ]) ; this is 'delta' is not 'increment'!
  (global-set-key (kbd "C-x g delta SPC") [?δ])
  (global-set-key (kbd "C-x g Delta SPC") [?Δ]) ; this is 'delta' is not 'increment'!


  (global-set-key (kbd "C-x g g SPC") [?γ])
  (global-set-key (kbd "C-x g G SPC") [?Γ])
  (global-set-key (kbd "C-x g gamma SPC") [?γ])
  (global-set-key (kbd "C-x g Gamma SPC") [?Γ])

  (global-set-key (kbd "C-x g l SPC") [?λ])
  (global-set-key (kbd "C-x g L SPC") [?Λ])
  (global-set-key (kbd "C-x g lambda SPC") [?λ])
  (global-set-key (kbd "C-x g Lambda SPC") [?Λ])

  (global-set-key (kbd "C-x g p SPC") [?π])
  (global-set-key (kbd "C-x g P SPC") [?Π])
  (global-set-key (kbd "C-x g pi SPC") [?π])
  (global-set-key (kbd "C-x g Pi SPC") [?Π])

  (global-set-key (kbd "C-x g > = SPC") [?≥])
  (global-set-key (kbd "C-x g < = SPC") [?≤])
  (global-set-key (kbd "C-x g ! = SPC") [?≠])
  (global-set-key (kbd "C-x g neq SPC") [?≠])
      
  (global-set-key (kbd "C-x g nil SPC") [?∅])

  (global-set-key (kbd "C-x g not SPC") [?¬])

  (global-set-key (kbd "C-x g and SPC") [?∧])
  (global-set-key (kbd "C-x g or SPC") [?∨])

  (global-set-key (kbd "C-x g exists SPC") [?∃])
  (global-set-key (kbd "C-x g all SPC") [?∀])

  (global-set-key (kbd "C-x g do SPC") [?⟳]) ; do
  (global-set-key (kbd "C-x g rb SPC") [?◨])
  (global-set-key (kbd "C-x g lb SPC") [?◧])

  (global-set-key (kbd "C-x g cont SPC") [?➜]) ; continue
  (global-set-key (kbd "C-x g thread SPC") [?☥]) ; thread

  (global-set-key (kbd "C-x g in SPC") [?∈]) ; set membership

;;--------------------------------------------------------------------------------
;; turn off the annoying bell
;;
;; (setq ring-bell-function (lambda ()
;;                            (call-process-shell-command
;;                              "xset led 3; xset -led 3" nil 0 nil)))
;;
;; (setq ring-bell-function nil)

 (setq ring-bell-function
       (lambda ()
	 (call-process-shell-command "xset led named 'Scroll Lock'")
	 (call-process-shell-command "xset -led named 'Scroll Lock'")))


;;--------------------------------------------------------------------------------
;; dirtrack
;;
;; get the pwd in shell mode from the prompt rather than guessing by
;; watching the commands typed .. yes! now shell variables and source
;; scripts will work
;;   in bashrc: export PS1='\n$(/usr/local/bin/Z)\u@\h§\w§\n> '
;;
  (add-hook 'shell-mode-hook
           (lambda ()
             (shell-dirtrack-mode -1)
             (dirtrack-mode 1)))

  (add-hook 'dirtrack-directory-change-hook
            (lambda ()
              (message default-directory)))

  (setq dirtrack-list '("§\\(.*\\)§\n> " 1))

;;--------------------------------------------------------------------------------
;; emacs behavior

  ;; use a backrevs dir rather than leaving ~file droppings everywhere
  ;;
    (setq backup-directory-alist `(("." . "~/emacs_backrevs")))
    (setq backup-by-copying t)

  ;; stop the 'tab' character polution
  ;;
    (setq-default indent-tabs-mode nil)

  ;; turn off the poison C-z key.  Use C-x C-z or the command suspend-emacs
  ;;
    (global-set-key (kbd "C-z") nil)

  ;; truncate rather than wrapping lines (use horizontal scroll to see to the right)
  ;;
    (set-default 'truncate-lines t)
    (setq truncate-partial-width-windows nil)
    (setq-default fill-column 90)
    (setq fill-column 90)

  ;; recover some window real estate
  ;;   c-x mode-line to toggle the mode-line on and off
  ;;
    (defun mode-line () "toggles the modeline on and off"
      (interactive) 
      (setq mode-line-format
        (if (equal mode-line-format nil)
            (default-value 'mode-line-format)) )
      (redraw-display))

    (tool-bar-mode -1)
    (menu-bar-mode -1)


  (put 'upcase-region 'disabled nil)
  (put 'narrow-to-region 'disabled nil)
  (put 'downcase-region 'disabled nil)
  (put 'set-goal-column 'disabled nil)
  (put 'erase-buffer 'disabled nil)

;(setq browse-url-browser-function 'browse-url-firefox)
(setq browse-url-browser-function 'browse-url-chrome)

;; vertical split for ediff
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
  '(ansi-color-names-vector
     ["#212526" "#ff4b4b" "#b4fa70" "#fce94f" "#729fcf" "#e090d7" "#8cc4ff" "#eeeeec"])
 '(custom-enabled-themes (quote (wheatgrass)))
 '(ediff-diff-options "-w")
 '(ediff-split-window-function (quote split-window-horizontally))
 '(ediff-window-setup-function (quote ediff-setup-windows-plain))
 '(geiser-racket-binary "racket")
 '(package-selected-packages (quote (markdown-mode rust-mode)))
 '(send-mail-function (quote smtpmail-send-it))
 '(tool-bar-mode nil))

;;--------------------------------------------------------------------------------
;; stuff the emacs menus put here
;;



(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "DejaVu Sans Mono" :foundry "PfEd" :slant normal :weight bold :height 98 :width normal)))))


