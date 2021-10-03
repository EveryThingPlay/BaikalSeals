//
//  ContactsView.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import Foundation
import UIKit

class ContactsView: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.cornerRadius = 15
        self.layer.shadowColor = UIColor(red: 0, green: 0, blue: 0, alpha: 0.5).cgColor
        self.layer.shadowOpacity = 1
        self.layer.shadowRadius = 6
        self.layer.shadowOffset = CGSize.zero
        

    }
}
