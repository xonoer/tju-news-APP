package Project;
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
	            //Document document = new Document("x",1);
	            //collection.insertOne(document);
	            //document.append("x",2).append("y",3);
	            BasicDBObject filter_dbobject = new BasicDBObject();

	            filter_dbobject.put("Kind", type);

	            List<Document> list  = collection.find(filter_dbobject).sort(new BasicDBObject("Time",-1)).skip(num*(page-1)).limit(num).into(new ArrayList<Document>());

	            for( Document l : list)
	            {
	                l.remove("_id");
	                //System.out.println(l.toJson());
	                String j = l.toJson();
	                //System.out.println(j);
	                JsonParser parser = new JsonParser();
	                JsonObject object = (JsonObject) parser.parse(j);
	                jsonArray.add(object);
	               // System.out.println(object);
	            }
	            
	            //MongoCursor<Document> cursor = collection.find(Filters.eq("x",1)).iterator();
	            //try{
	            //    while (cursor.hasNext())
	            //        //System.out.println(cursor.next().toJson() + "hello");
	            //}finally {
	            //    cursor.close();
	           // }

	            mongo.close();
	            
	        }catch (Exception e)
	        {
	            System.out.println(e);
	        }
		return jsonArray;
	}
}
