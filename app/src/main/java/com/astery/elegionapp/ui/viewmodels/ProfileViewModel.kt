package com.astery.elegionapp.ui.viewmodels

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.astery.elegionapp.data_source.local.database.db_utils.LocalLoadable
import com.astery.elegionapp.pojo.User
import com.astery.elegionapp.repository.Repository
import com.astery.elegionapp.ui.adapters.units.*

class ProfileViewModel: ViewModel() {

    val user: LiveData<User> = MutableLiveData()

    internal var repository:Repository? = null


    fun getData(){
        repository?.getValue(user, User::class.java)
    }
}