# util 说明

<!-- TOC depthFrom:2 -->

- [String为空](#string为空)
- [比较两个日期的大小](#比较两个日期的大小)

<!-- /TOC -->

## String为空

```java
    /**
	 * 判断字符串是否为空
	 * 
	 * @param str
	 * @return 空 :true | 非空 :false
	 */
	public static Boolean stringIsempty(String str) {
		if (null == str || "".equals(str)) {
			return true;
		} else {
			return false;
		}
	}
```

## 比较两个日期的大小

```java
```