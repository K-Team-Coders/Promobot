package com.dis.veles;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.fragment.app.Fragment;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;
public class fragment_search extends Fragment implements View.OnClickListener {
    public Button searchBtn;
    public EditText coment;
    public TextView date;
    public TextView group_them;
    public TextView them;
    public TextView locate;
    public TextView organisator;
    public String URL = "https://79vsn76k-8000.euw.devtunnels.ms/api/add_message_all_pavlov";
    public String message;
    public String Get;
    public String coord;


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View v = inflater.inflate(R.layout.fragment_activity_search, container, false);

        date = v.findViewById(R.id.date);
        group_them = v.findViewById(R.id.group);
        them = v.findViewById(R.id.them);
        locate = v.findViewById(R.id.locate);
        organisator = v.findViewById(R.id.org);

        searchBtn = (Button) v.findViewById(R.id.searchBTN);
        coment = (EditText) v.findViewById(R.id.field);
        searchBtn.setOnClickListener(this);
        return v;
    }
    @Override
    public void onClick(View v) {
        Handler handler = new Handler(Looper.getMainLooper());
        if (coment.getText().toString().isEmpty() ) {
            Toast.makeText(getActivity(), "Пожалуйста ввидите значаение", Toast.LENGTH_SHORT).show();
            return;
        }else {message=coment.getText().toString();}
        new Thread(new Runnable() {
     @Override
     public void run() {
             MediaType JSON = MediaType.get("application/json; charset=utf-8");
             JSONObject jsonRequest = new JSONObject();
             try {
                 jsonRequest.put("message", message);
             } catch (JSONException e) {
                 throw new RuntimeException(e);
             }
             OkHttpClient client = new OkHttpClient();
             RequestBody body = RequestBody.create(JSON, jsonRequest.toString());
             Request.Builder requestBuilder = new Request.Builder().url(URL).post(body);
             Request request = requestBuilder.build();

             try (Response response = client.newCall(request).execute()) {
                 if (!response.isSuccessful()) {
                     throw new IOException("Запрос к серверу не был успешен: " +
                             response.code() + " " + response.message());
                 }
                 //System.out.println(response.body().string());
                 Get = response.body().string();
                 handler.post(() -> {
                     JSONObject jsnobject = null;
                     try {
                         jsnobject = new JSONObject(Get);
                     } catch (JSONException e) {
                         throw new RuntimeException(e);
                     }
                     try {
                         date.setText(jsnobject.get("date").toString());
                         group_them.setText(jsnobject.get("group").toString());
                         them.setText(jsnobject.get("theme").toString());
                         JSONArray jsonArray = jsnobject.getJSONArray("loc");
                         //JSONArray jsonArray = jsnobject.getJSONArray("coords");
                         locate.setText(jsonArray.toString());

                         organisator.setText(jsnobject.get("organisation").toString());

                     } catch (JSONException e) {
                         throw new RuntimeException(e);
                     }
                 });

             } catch (IOException e) {
                 System.out.println("Ошибка подключения: " + e);
             }
         }
 }).start();


    }




    }


