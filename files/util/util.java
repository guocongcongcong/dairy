public class CommonUtil {

	/**
	 * 判断字符串是否为空
	 * 
	 * @param str
	 * @return 空 :true | 非空 :false
	 */
	public static Boolean StringIsempty(String str) {
		if (null == str || "".equals(str)) {
			return true;
		} else {
			return false;
		}
	}
}
