import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.concurrent.TimeUnit;

import java.util.Random;

import javax.websocket.OnClose;
import javax.websocket.OnError;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.server.ServerEndpoint;

import org.omg.CORBA.portable.InputStream;
import org.omg.CORBA.portable.OutputStream;

import com.sun.corba.se.spi.orbutil.fsm.InputImpl;


@ServerEndpoint("/communicate")
public class ServerSocket 
{	
	@OnOpen
	public void handleOpen(){
		System.out.println("Client Connected...");
	}
	@OnMessage
	public String handleMessage(String message) throws IOException{
		System.out.println("received from clent: "+ message);
		
//		String reply = "echo "+ message;
		message = getAndSendData();
		System.out.println("Sent to clent: "+ message);	
		return message;
	}
	public String getAndSendData() throws IOException 
	{
		System.out.println("entered the getAndSendData function");
		Random rand = new Random();
//		int  n = rand.nextInt(10) + 5;
		int q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20;
		q1 = rand.nextInt(10) + 5;
		q2 = rand.nextInt(10) + 5;
		q3 = rand.nextInt(10) + 5;
		q4 = rand.nextInt(10) + 5;
		q5 = rand.nextInt(10) + 5;
		q6 = rand.nextInt(10) + 5;
		q7 = rand.nextInt(10) + 5;
		q8 = rand.nextInt(10) + 5;
		q9 = rand.nextInt(10) + 5;
		q10 = rand.nextInt(10) + 5;
		q11 = rand.nextInt(10) + 5;
		q12 = rand.nextInt(10) + 5;
		q13 = rand.nextInt(10) + 5;
		q14 = rand.nextInt(10) + 5;
		q15 = rand.nextInt(10) + 5;
		q16 = rand.nextInt(10) + 5;
		q17 = rand.nextInt(10) + 5;
		q18 = rand.nextInt(10) + 5;
		q19 = rand.nextInt(10) + 5;
		q20 = rand.nextInt(10) + 5;
		int t = q1 + Math.min(Math.min(q2, q3), q4) + Math.min(q5, q6) + q7;
		int t1 = q8 + Math.min(Math.min(q9, q10), q11) + Math.min(q12, q13) + q14;
		int total = Math.min(t, t1);
		StringBuilder str = new StringBuilder(0);
		str.append("{\"Queue1\":\"");
		str.append(q1);
		str.append(" min\", \"Queue2\":\"");
		str.append(q2);
		str.append(" min\", \"Queue3\":\"");
		str.append(q3);
		str.append(" min\", \"Queue4\":\"");
		str.append(q4);
		str.append(" min\", \"Queue5\":\"");
		str.append(q5);
		str.append(" min\", \"Queue6\":\"");
		str.append(q6);
		str.append(" min\", \"Queue7\":\"");
		str.append(q7);
		str.append(" min\", \"Queue8\":\"");
		str.append(q8);
		str.append(" min\", \"Queue9\":\"");
		str.append(q9);
		str.append(" min\", \"Queue10\":\"");
		str.append(q10);
		str.append(" min\", \"Queue11\":\"");
		str.append(q11);
		str.append(" min\", \"Queue12\":\"");
		str.append(q12);
		str.append(" min\", \"Queue13\":\"");
		str.append(q13);
		str.append(" min\", \"Queue14\":\"");
		str.append(q14);
		str.append(" min\", \"Queue15\":\"");
		str.append(q15);
		str.append(" min\", \"Queue16\":\"");
		str.append(q16);
		str.append(" min\", \"Queue17\":\"");
		str.append(q17);
		str.append(" min\", \"Queue18\":\"");
		str.append(q18);
		str.append(" min\", \"Queue19\":\"");
		str.append(q19);
		str.append(" min\", \"Queue20\":\"");
		str.append(q20);
		str.append(" min\", \"TotalTime\":\"");
		str.append(total);
		str.append(" min\"}");
//		return "{\"Queue1\":\"10 min\", \"Queue2\":\"15 min\"}";
		System.out.println("done with this" + str.toString());
		return str.toString();
	}
	@OnClose
	public void handleClose(){
		System.out.println("Client Disconnected.");
	}
	@OnError
	public void handleError(Throwable t){
		t.printStackTrace();
	}
	public void main(String arrgs[]) throws IOException
	{
		FileOutputStream f = new FileOutputStream("temp1.txt");
		f.write(123);
		f.close();
		System.out.println("enter 1");
	}
}