//
//  UserPathVC.swift
//  E-legion
//
//  Created by Сергей Чумовских  on 02.10.2021.
//

//    AddSkill segue

import UIKit

class UserPathVC: UIViewController {

    @IBOutlet private var namePathLabel: UILabel!
    @IBOutlet private var target1Label: UILabel!
    @IBOutlet private var target2Label: UILabel!
    @IBOutlet private var target1Button: CheckButton!
    @IBOutlet private var target2Button: CheckButton!
    @IBOutlet private var task1Label: UILabel!
    @IBOutlet private var task2Label: UILabel!
    @IBOutlet private var task3Label: UILabel!
    @IBOutlet private var task1Button: CheckButton!
    @IBOutlet private var task2Button: CheckButton!
    @IBOutlet private var task3Button: CheckButton!
    @IBOutlet private var skill1Label: UILabel!
    @IBOutlet private var skill2Label: UILabel!
    @IBOutlet private var skill3Label: UILabel!
    @IBOutlet private var skill1Button: CheckButton!
    @IBOutlet private var skill2Button: CheckButton!
    @IBOutlet private var skill3Button: CheckButton!
    
    @IBOutlet var skilsLabel: UILabel!
    
    @IBOutlet var addSkillButton: AddSkillButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        guard segue.identifier == "changeMyTarget",
              let vc = segue.destination as? MyTargetVC,
              let send = sender as? String
        else {return}
        vc.targetName = send
    }

    @IBAction func addSkillButtonTaped(_ sender: UIButton) {
        performSegue(withIdentifier: "AddSkill", sender: nil)
        
    }
    
    @IBAction func targetButtonTap(_ sender: UIButton) {
        // send to back
        performSegue(withIdentifier: "changeMyTarget", sender: target1Label.text)
    }
    
    @IBAction func target2ButtonTap(_ sender: UIButton) {
        performSegue(withIdentifier: "changeMyTarget", sender: target2Label.text)
    }
    
    @IBAction func gearButtonTap(_ sender: Any) {
        performSegue(withIdentifier: "goToProfile", sender: nil)
        // send to user.session back
        // get user.info
    }
    
    @IBAction func taskButtonTap(_ sender: Any) {
        // send to back
    }
    
    @IBAction func skillButtonTap(_ sender: Any) {
        // send to back
    }
    
}
