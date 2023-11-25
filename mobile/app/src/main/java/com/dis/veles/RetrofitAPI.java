package com.dis.veles;
import retrofit2.Call;
        import retrofit2.http.Body;
        import retrofit2.http.POST;

public interface RetrofitAPI {
    @POST("")
    Call<DataModal> createPost(@Body DataModal dataModal);
}
