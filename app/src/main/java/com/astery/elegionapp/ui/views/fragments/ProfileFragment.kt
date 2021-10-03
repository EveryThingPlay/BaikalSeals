package com.astery.elegionapp.ui.views.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.View.GONE
import android.view.ViewGroup
import androidx.fragment.app.viewModels
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView.VERTICAL
import com.astery.elegionapp.R
import com.astery.elegionapp.architecture.App
import com.astery.elegionapp.data_source.local.database.db_utils.LocalLoadable
import com.astery.elegionapp.databinding.FragmentProfileBinding
import com.astery.elegionapp.databinding.FragmentRequestsBinding
import com.astery.elegionapp.ui.adapters.ProfileAdapter
import com.astery.elegionapp.ui.adapters.RequestAdapter
import com.astery.elegionapp.ui.adapters.VacationAdapter
import com.astery.elegionapp.ui.adapters.forms_adapter.EditTextElement
import com.astery.elegionapp.ui.adapters.forms_adapter.FormsAdapter
import com.astery.elegionapp.ui.adapters.forms_adapter.LongEditTextElement
import com.astery.elegionapp.ui.adapters.forms_adapter.SpinnerElement
import com.astery.elegionapp.ui.adapters.units.Profile
import com.astery.elegionapp.ui.adapters.units.Request
import com.astery.elegionapp.ui.adapters.units.Vacation
import com.astery.elegionapp.ui.viewmodels.ProfileViewModel
import com.astery.elegionapp.ui.viewmodels.VacationViewModel
import com.astery.elegionapp.ui.views.XFragment
import com.astery.elegionapp.ui.views.utils.BlockableBundle
import com.astery.elegionapp.ui.views.utils.FormDialogue
import java.util.ArrayList

/** */
class ProfileFragment : XFragment() {

    private lateinit var thisBinding:FragmentProfileBinding

    private val viewModel: ProfileViewModel by viewModels()


    private lateinit var contactAdapter: ProfileAdapter
    private lateinit var occupationAdapter: ProfileAdapter
    private lateinit var otherAdapter: ProfileAdapter


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        bind = FragmentProfileBinding.inflate(inflater, container, false)
        thisBinding = binding as FragmentProfileBinding
        return binding.root
    }




    override fun prepareAdapters(){
        this.contactAdapter = ProfileAdapter(this, thisBinding.contacts.contactsElements)
        //this.occupationAdapter = ProfileAdapter(this, thisBinding.occupation.occupationElements)
        this.otherAdapter = ProfileAdapter(this, thisBinding.other.otherElement)
    }

    override fun setViewModelListeners() {
        viewModel.repository = (requireActivity().application as App).container.repository
        viewModel.getData()

        viewModel.user.observe(viewLifecycleOwner, {
            t ->
            run {
                thisBinding.head.name.text = t.name
                thisBinding.head.fam.text = t.surname
                thisBinding.head.father.text = t.lastName
                thisBinding.head.occupation.text = t.role

                contactAdapter.add(Profile("Телеграм", t.telegram))
                contactAdapter.add(Profile("Email", t.email))
                contactAdapter.add(Profile("Телефон", t.phone))

                /*
                occupationAdapter.add(Profile("Руководитель отдела", t.manager))
                occupationAdapter.add(Profile("Медеджер пропусков", t.passManager))
                occupationAdapter.add(Profile("Офис", t.office))
                occupationAdapter.add(Profile("Подразделение", t.division))
                occupationAdapter.add(Profile("Трудоустроен", t.employment))
                occupationAdapter.add(Profile("Должность", t.role))

                 */

                otherAdapter.add(Profile("Пол", "Мужской"))
            }
        })
    }

    override fun setListeners() {
    }

    override fun onBackPressed(): Boolean {
        return false
    }

    override fun getTitle(): String? {
        return getString(R.string.title_profile)
    }
}