package server;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.gson.JsonArray;

/**
 * Servlet implementation class GetJson
 */
@WebServlet("/GetJson")
public class GetJson extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public GetJson() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		String kindStr = null;
		String pageStr = null;
		String numStr = null;
		int page = 1;
		int num = 5;
		String source = request.getParameter("source");
		if(request.getParameter("kind") != null){
			kindStr = request.getParameter("kind");
		}
		if(request.getParameter("page") != null){
			pageStr = request.getParameter("page");
			page = Integer.parseInt(pageStr);
		}
		if(request.getParameter("num") != null){
			numStr = request.getParameter("num");
			num = Integer.parseInt(numStr);
		}
		JsonArray jsonArray = new JsonArray();
		if(source.equals("twtURL")){
			if(kindStr != null){
				jsonArray = functions.getData(source,kindStr,page,num);
			}else{
				jsonArray = functions.getData(source,page,num);
			}
		}else if(source.equals("tju")){
			if(kindStr != null){
				jsonArray = functions.getData(source,kindStr,page,num);
			}else{
				jsonArray = functions.getData(source,page,num);
			}
		}
		
		
		
		
		response.setContentType("application/json");
		response.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();  
        out.write(jsonArray.toString());
        out.flush();
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
