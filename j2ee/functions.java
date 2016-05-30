import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCursor;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;

import org.bson.Document;

import java.util.ArrayList;
import java.util.List;
public class functions {
	public static JsonArray getData(String type,int page,int num) {
		JsonArray jsonArray = new JsonArray();   
		try {
	            MongoClient mongo = new MongoClient("localhost", 27017);
	            MongoDatabase db = mongo.getDatabase("test");
	            MongoCollection<Document> collection = db.getCollection("result");
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
}
