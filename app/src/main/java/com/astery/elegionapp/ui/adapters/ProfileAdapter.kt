package com.astery.elegionapp.ui.adapters

import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.fragment.app.Fragment
import com.astery.elegionapp.R
import com.astery.elegionapp.pojo.User
import com.astery.elegionapp.ui.adapters.forms_adapter.ChangeBranchListener
import com.astery.elegionapp.ui.adapters.forms_adapter.FormElement
import com.astery.elegionapp.ui.adapters.forms_adapter.FormsAdapter
import com.astery.elegionapp.ui.adapters.forms_adapter.SpinnerElement
import com.astery.elegionapp.ui.adapters.units.Profile
import com.astery.elegionapp.ui.adapters.units.Task
import com.astery.elegionapp.ui.views.utils.SD
import com.google.android.material.textfield.TextInputEditText


class ProfileAdapter(val parent: Fragment, var form:ViewGroup) {
    var units:ArrayList<Profile> = ArrayList()

    fun update(){
        form.removeAllViews()
        draw(units)
    }

    fun add(unit :Profile){
        units.add(unit)

        val view = parent.layoutInflater.inflate(R.layout.unit_profile_item, null) as LinearLayout
        view.findViewById<TextView>(R.id.title).text = unit.title
        view.findViewById<TextView>(R.id.value).text = unit.value

        form.addView(view)

    }

    fun draw(units: List<Profile>) {
        this.units = ArrayList()
        for (i in units.indices) {
            add(units[i])
        }
    }

}