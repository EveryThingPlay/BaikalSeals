//
//  ImageAvatar.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import Foundation
import UIKit

class ImageAvatar: UIImageView {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.cornerRadius = self.frame.height/2
        self.layer.shadowColor = UIColor(red: 0, green: 0.682, blue: 0.937, alpha: 0.1).cgColor
        self.layer.shadowOpacity = 1
        self.layer.shadowRadius = 5
        self.layer.shadowOffset = CGSize.zero
    }
}
