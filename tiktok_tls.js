
Java.perform(function() {
    var className = "X.T7d";
    var methodName = "LJIIIIZZ";
    var targetClass = Java.use(className);
    targetClass[methodName].overload('X.T7e', 'java.lang.String', '[B', 'android.content.Context', 'boolean', '[Ljava.lang.String;', 'java.util.Map', 'java.lang.String', 'boolean', 'boolean').implementation = function(r4, r5, r6, r7, r8, r9, r10, r11, r12, r13) {
        console.log("Hooked LJIIIIZZ method successfully");
        var result = this[methodName].apply(this, arguments);
        console.log(result)
        return result;
    };
});

Java.perform(function () {
    var className = "X.T8u"; 
    var classToHook = Java.use(className);
    var constructor = classToHook.$init.overload('[Ljava.lang.String;', '[Ljava.lang.String;', '[Ljava.lang.String;', '[Ljava.lang.String;');
    constructor.implementation = function (strArr, strArr2, strArr3, strArr4) {
        console.log("Original this.LJ values: " + strArr3);
        var strArr3 = ["https://tls.peet.ws/api/all", "https://tls.peet.ws/api/all"];
        var instance = constructor.apply(this, [strArr, strArr2, strArr3, strArr4]);
        return instance;
    };
});

