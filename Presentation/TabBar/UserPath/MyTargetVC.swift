//
//  MyTargetVC.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//
// segue changeMyTarget

import UIKit

class MyTargetVC: UIViewController {

    @IBOutlet private var contentView: UIView!
    @IBOutlet private var targetNameLabel: UILabel!
    @IBOutlet private var textView: UITextView!
    @IBOutlet private var addFileButton: CusomButton!
    @IBOutlet private var sendPostButton: CusomButton!
    
    private var tapGesture: UITapGestureRecognizer?
    
    var targetName: String?

    override func viewDidLoad() {
        super.viewDidLoad()
        targetNameLabel.text = targetName
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

    @IBAction func addFileButtonTap(_ sender: UIButton) {
        //open file
        //or paste link
    }
    
    @IBAction func sendPostButtonTap(_ sender: UIButton) {
        //send to backend targetNameLabel.text
        //send to backend textView.text
        //send to backend fileNameLabel
    }
    
}
