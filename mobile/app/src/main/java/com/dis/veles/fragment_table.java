package com.dis.veles;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentResultListener;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;

public class fragment_table extends Fragment {

    public String USER_API = "https://api.jsonserve.com/MpiapF";
    public TextView coords;

    // contacts JSONArray

    ArrayList<Card> cards = new ArrayList<Card>();

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View v = inflater.inflate(R.layout.fragment_activity_table, container, false);

        String message ="rm";
        coords = v.findViewById(R.id.coords);
        coords.setText(message);







        return v;
    }
}


