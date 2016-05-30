import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.common.base.Function;
import com.google.common.base.Functions;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import org.bson.Document;

import java.util.ArrayList;
import java.util.List;

public class Select extends HttpServlet {

	public Select() {
		super();
	}
	public void destroy() {
		super.destroy();
	}

	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String typeString = request.getParameter("type");
		String pageString = request.getParameter("page");
		String numString = request.getParameter("num");
		int page = Integer.parseInt(pageString);
		int num = Integer.parseInt(numString);
		JsonArray jsonArray = functions.getData(typeString,page,num);

		response.setContentType("application/json");
		esponse.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();  
        out.write(jsonArray);
        out.flush();
	}

	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request,response);
	}

}
