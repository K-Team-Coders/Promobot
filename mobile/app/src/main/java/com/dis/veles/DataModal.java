package com.dis.veles;

import org.json.JSONObject;

public class DataModal {
    // string variables for our name and job
    private JSONObject txt;


    public DataModal(JSONObject txt) {
        this.txt = txt;
    }

    public JSONObject getTxt() {
        return txt;
    }

    public void setTxt(JSONObject txt) {
        this.txt = txt;
    }


}
