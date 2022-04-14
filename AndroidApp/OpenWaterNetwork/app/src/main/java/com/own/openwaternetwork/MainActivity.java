package com.own.openwaternetwork;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {

    private WebView p_VW1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        p_VW1 = (WebView)findViewById(R.id.webView);
        WebSettings l_ws = p_VW1.getSettings();
        l_ws.setJavaScriptEnabled(true);
        p_VW1.loadUrl("https://openwater.network:8890/dashboard/ea94d0f0-33e9-11eb-b6b6-098388a31d5f?publicId=3ee96010-204b-11eb-b6b6-098388a31d5f");
        p_VW1.setWebViewClient(new WebViewClient());
    }

    @Override
    public void onBackPressed() {
        if (p_VW1.canGoBack()){
            p_VW1.goBack();
        } else {
            super.onBackPressed();
        }

    }
}