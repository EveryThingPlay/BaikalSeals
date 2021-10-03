//
//  ViewProfile.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import Foundation
import UIKit

class ViewProfile: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()
        self.layer.masksToBounds = true
        self.layer.cornerRadius = 13.5
    }
}
