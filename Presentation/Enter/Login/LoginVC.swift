//
//  LoginVC.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 28.09.2021.
//

import Foundation
import UIKit

class LoginVC: UIViewController, UITextFieldDelegate {
    
    @IBOutlet private var loginButton: CusomButton2!
    @IBOutlet private var regButton: CusomButton!
    @IBOutlet private var alertLabel: UILabel!
    @IBOutlet private var phoneTextField: TextField!
    @IBOutlet private var passTextField: TextField!
    @IBOutlet private var scrollView: UIScrollView!
    @IBOutlet private var visibleView: UIView!
    
    private var tapGesture: UITapGestureRecognizer?
    
    var failLogin: Bool = false
    
    override func viewDidLoad() {
        super.viewDidLoad()
        passTextField.delegate = self
        phoneTextField.delegate = self
        setMyTap()
        changeText()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        // Подписываемся на два уведомления: одно приходит при появлении клавиатуры
        NotificationCenter.default.addObserver(self, selector: #selector(self.keyboardWasShown),
                                               name: UIResponder.keyboardWillShowNotification, object: nil)
        // Второе — когда она пропадает
        NotificationCenter.default.addObserver(self, selector: #selector(self.keyboardWillBeHidden(notification:)),
                                               name: UIResponder.keyboardWillHideNotification, object: nil)
    }
    
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        // Отписываемся от уведомлений клавиатуры
        NotificationCenter.default.removeObserver(self, name: UIResponder.keyboardWillShowNotification, object: nil)
        NotificationCenter.default.removeObserver(self, name: UIResponder.keyboardWillHideNotification, object: nil)
        
    }
    
    private func setMyTap() {
        tapGesture = UITapGestureRecognizer(target: self, action: #selector(hideKeyboard))
        visibleView.addGestureRecognizer(tapGesture!)
    }
    
    // изменим текс на placeholder
    private func changeText() {
        phoneTextField.placeholder = phoneTextField.text
        phoneTextField.text = nil
        passTextField.placeholder = passTextField.text
        passTextField.text = nil
    }
    
    @objc private func keyboardWasShown(notification: Notification) {
        // Когда клавиатура появляется
        // Получаем размер клавиатуры
        let info = notification.userInfo! as NSDictionary
        let kbSize = (info.value(forKey: UIResponder.keyboardFrameEndUserInfoKey) as! NSValue).cgRectValue.size
        let contentInsets = UIEdgeInsets(top: 0.0, left: 0.0, bottom: kbSize.height, right: 0.0)
        // Добавляем отступ внизу UIScrollView, равный размеру клавиатуры
        self.scrollView?.contentInset = contentInsets
        scrollView?.scrollIndicatorInsets = contentInsets
    }
    
    @objc private func keyboardWillBeHidden(notification: Notification) {
        //Когда клавиатура исчезает
        // Устанавливаем отступ внизу UIScrollView, равный 0
        let contentInsets = UIEdgeInsets.zero
        scrollView?.contentInset = contentInsets
        scrollView?.scrollIndicatorInsets = contentInsets
    }
    
    @objc private func hideKeyboard() {
        self.visibleView?.endEditing(true)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard segue.identifier == "LoginToBar"  else {return}
    }
        
    // test login
    @IBAction func loginButtonTap(_ sender: UIButton) {
        guard phoneTextField.text == "0",
              passTextField.text == "0"
        else {
            alertLabel.isHidden = false
            loginButton.setTitle("Забыли пароль?", for: .normal)
            failLogin = true
            return
        }
        performSegue(withIdentifier: "LoginToBar", sender: nil)
    }
    
    func textFieldDidBeginEditing(_ textField: UITextField) {
        guard failLogin else { return }
        loginButton.setTitle("Войти", for: .normal)
    }
    
    
    @IBAction func regButtonTap(_ sender: UIButton) {
    }
}
