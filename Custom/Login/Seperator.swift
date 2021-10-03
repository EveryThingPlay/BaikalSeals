//
//  Seperator.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import Foundation
import UIKit

class Seperator: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.masksToBounds = true
        self.layer.cornerRadius = 1
        self.layer.backgroundColor = UIColor(red: 0.824, green: 0.831, blue: 0.847, alpha: 1).cgColor
    }
}
