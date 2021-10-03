//
//  CustomButton3.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 01.10.2021.
//

import Foundation
import UIKit

class CusomButton3: UIButton {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.borderColor = #colorLiteral(red: 0.701890409, green: 0.7020100951, blue: 0.7018746734, alpha: 1)
        self.layer.borderWidth = 4
        self.layer.cornerRadius = 10
    }
}
