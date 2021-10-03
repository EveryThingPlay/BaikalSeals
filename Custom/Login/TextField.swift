//
//  TextField.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 01.10.2021.
//

import Foundation
import UIKit

class TextField: UITextField {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.borderColor = #colorLiteral(red: 0.8216689229, green: 0.8317583203, blue: 0.8486261368, alpha: 1)
        self.layer.borderWidth = 1
        self.layer.cornerRadius = 5
//        self.font = UIFont(name: "Montserrat-Regular", size: 18)
    }
}
