//
//  PropertySkillViewController.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import UIKit

class PropertySkillVC: UIViewController {

    @IBOutlet private var contentView: UIView!
    @IBOutlet private var textView: UITextView!
    @IBOutlet private var addFileButton: CusomButton!
    @IBOutlet private var sendPostButton: CusomButton!
    @IBOutlet private var fileImage: UIImageView!
    @IBOutlet private var fileNameLabel: UILabel!
    @IBOutlet private var nameSkillTextField: UITextField!
    
    private var tapGesture: UITapGestureRecognizer?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setMyTap()
    }
    
    // for hide keyboard
    private func setMyTap() {
        tapGesture = UITapGestureRecognizer(target: self, action: #selector(hideKeyboard))
        contentView.addGestureRecognizer(tapGesture!)
    }
    
    @objc private func hideKeyboard() {
        self.contentView?.endEditing(true)
    }
    
    
    @IBAction func addFileButtonTap(_ sender: Any) {
        //open file
        //or paste link
        //fileImage.image change
    }
    
    
    @IBAction func sendPostButtonTap(_ sender: Any) {
        //send to backend nameSkillTextField.text
        //send to backend textView.text
        //send to backend file
    }
    
    
}
