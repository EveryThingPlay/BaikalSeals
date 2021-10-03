//
//  Plug.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 03.10.2021.
//

import UIKit

class Plug: UIViewController {
    
    private var displayLink: CADisplayLink?
    private var loadingLabeltext: String = ""
    private var loadingLabel: UILabel = {
        let label = UILabel()
        label.textColor = UIColor.black
        label.textAlignment = .center
        label.font = UIFont.boldSystemFont(ofSize: 40)
        return label
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setView()
    }
    
    private func setView() {
        view.addSubview(loadingLabel)
        loadingLabel.text = "Loading ..."
        loadingLabel.frame = view.frame
        animateLabelDots(label: loadingLabel)
    }
    
    private func animateLabelDots(label: UILabel) {
        guard var text = label.text else { return }
        text = String(text.dropLast(3))
        loadingLabeltext = text
        displayLink = CADisplayLink(target: self, selector: #selector(showHideDots))
        displayLink?.add(to: .main, forMode: .common)
        displayLink?.preferredFramesPerSecond = 2
    }
    
    @objc private func showHideDots() {
        if !loadingLabeltext.contains("...") {
            loadingLabeltext = loadingLabeltext.appending(".")
        } else {
            loadingLabeltext = "Loading "
        }
        loadingLabel.text = loadingLabeltext
    }

}
