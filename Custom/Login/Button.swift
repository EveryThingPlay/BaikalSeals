//
//  Button.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 01.10.2021.
//

import Foundation
import UIKit

class CusomButton: UIButton {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.borderColor = #colorLiteral(red: 0, green: 0.6809337735, blue: 0.9363232851, alpha: 1)
        self.layer.borderWidth = 4
        self.layer.cornerRadius = 10
    }
}
