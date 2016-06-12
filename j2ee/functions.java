package server;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.mongodb.BasicDBObject;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

import java.util.ArrayList;
import java.util.List;
public class functions {
	
	
	public static JsonArray getData(String source,String type,int page,int num) {
		JsonArray jsonArray = new JsonArray();   
		try {
	            MongoClient mongo = new MongoClient("localhost", 27017);
	            MongoDatabase db = mongo.getDatabase("test");
	            MongoCollection<Document> collection = db.getCollection(source);
	            BasicDBObject filter_dbobject = new BasicDBObject();
	            filter_dbobject.put("Kind", type);
	            List<Document> list  = collection.find(filter_dbobject).sort(new BasicDBObject("Time",-1)).skip(num*(page-1)).limit(num).into(new ArrayList<Document>());
	            for( Document l : list)
	            {
	                l.remove("_id");
	                String j = l.toJson();
	                JsonParser parser = new JsonParser();
	                JsonObject object = (JsonObject) parser.parse(j);
	                jsonArray.add(object);
	            }
	            mongo.close();
	        }catch (Exception e)
	        {
	            System.out.println(e);
	        }
		return jsonArray;
	}
	public static JsonArray getData(String source,int page, int num) {
		JsonArray jsonArray = new JsonArray();   
		try {
	            MongoClient mongo = new MongoClient("localhost", 27017);
	            MongoDatabase db = mongo.getDatabase("test");
	            MongoCollection<Document> collection = db.getCollection(source);
	            List<Document> list  = collection.find().sort(new BasicDBObject("Time",-1)).skip(num*(page-1)).limit(num).into(new ArrayList<Document>());
	            for( Document l : list)
	            {
	                l.remove("_id");
	                String j = l.toJson();
	                JsonParser parser = new JsonParser();
	                JsonObject object = (JsonObject) parser.parse(j);
	                jsonArray.add(object);
	            }
	            mongo.close();
	        }catch (Exception e)
	        {
	            System.out.println(e);
	        }
		return jsonArray;
	}
}