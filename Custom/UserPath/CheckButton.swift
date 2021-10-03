//
//  CheckButton.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import Foundation
import UIKit

class CheckButton: UIButton {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.addTarget(self, action: #selector(tapControl(_:)), for: .touchUpInside)
    }
    
    @objc func tapControl(_ sender: UIButton) {
        self.setImage(UIImage(systemName: "checkmark.square.fill"), for: .normal)
//        self.setImage(UIImage(systemName: "checkmark.square.fill"), for: .selected)
    }
    
}
