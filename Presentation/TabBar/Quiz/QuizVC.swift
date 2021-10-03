//
//  QuizVC.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

import UIKit

class QuizVC: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func allCheckButton1(_ sender: UIButton) {
        // отправить в бэк
    }
    @IBAction func allCheckButton2(_ sender: UIButton) {
        // отправить в бэк
    }
    @IBAction func allCheckButton3(_ sender: UIButton) {
        // отправить в бэк
    }
    
    @IBAction func showAllButton(_ sender: UIButton) {
        let alert = UIAlertController(title: "Вы нажали 'Показать все'", message: "Не спрашивайте откуда я знаю, просто я телепат", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        self.present(alert, animated: true, completion: nil)
        // принять список с бэка
        // или загрузить из хранилища
    }
    
    @IBAction func bonusCheckButton1(_ sender: UIButton) {
        // отправить в бэк
    }
    @IBAction func bonusCheckButton2(_ sender: UIButton) {
        // отправить в бэк
    }
    @IBAction func bonusCheckButton3(_ sender: UIButton) {
        // отправить в бэк
    }
    
    @IBAction func showBonusButton(_ sender: UIButton) {
        let alert = UIAlertController(title: "Вы открыли бонус-секцию", message: "Эта функция в доработке", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        self.present(alert, animated: true, completion: nil)
        // принять список с бэка
        // или загрузить из хранилища
    }
}
